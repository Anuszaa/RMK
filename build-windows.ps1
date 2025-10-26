# PowerShell script to build Windows exe using PyInstaller
param(
    [string]$Python = 'python',
    [string]$Spec = 'main.spec'
)

Write-Host "Installing PyInstaller..."
& $Python -m pip install --upgrade pip
& $Python -m pip install pyinstaller

Write-Host "Building EXE using spec: $Spec"

# Ensure build folder exists for logs and final copy
$buildRoot = Join-Path -Path "." -ChildPath "build"
if (-not (Test-Path $buildRoot)) {
    New-Item -ItemType Directory -Path $buildRoot -Force | Out-Null
}

$log = Join-Path -Path $buildRoot -ChildPath "pyinstaller.log"
Write-Host "Running PyInstaller (spec) and logging output to: $log"

# Run PyInstaller using the spec and tee output to log file
# Ensure data.json exists (PyInstaller will error if datas entry points to missing file)
$dataFile = Join-Path -Path "." -ChildPath "data.json"
if (-not (Test-Path $dataFile)) {
    Write-Host "data.json not found, creating minimal placeholder at: $dataFile"
    try {
        '{}' | Out-File -FilePath $dataFile -Encoding UTF8 -Force
        Write-Host "Created placeholder data.json"
    } catch {
        Write-Host "Failed to create data.json - Error: $($_.Exception.Message)"
    }
}

# Remove existing dist artifacts if present to avoid PermissionError during copy
$distOnefile = Join-Path -Path "dist" -ChildPath "RMK_insGT.exe"
$distOnedir = Join-Path -Path "dist" -ChildPath "RMK_insGT"
function Try-RemoveFile($path) {
    if (-not (Test-Path $path)) { return $true }
    Write-Host "Found existing artifact: $path"
    # Try to unset read-only / other attributes
    try {
        $item = Get-Item -LiteralPath $path -ErrorAction SilentlyContinue
        if ($item) {
            Write-Host "Clearing file attributes for: $path"
            $item.Attributes = 'Normal'
        }
    } catch {
        Write-Host "Warning - could not clear attributes - Error: $($_.Exception.Message)"
    }

    # Try to stop a running process named 'main' (common if exe is running)
    try {
        $proc = Get-Process -Name 'main' -ErrorAction SilentlyContinue
        if ($proc) {
            $pidList = $proc.Id -join ', '
            Write-Host "Attempting to stop running process 'main' (PIDs: $pidList)"
            Stop-Process -Id ($proc.Id) -Force -ErrorAction SilentlyContinue
            Start-Sleep -Milliseconds 200
        }
    } catch {
        Write-Host "Could not stop process 'main' - Error: $($_.Exception.Message)"
    }

    # Try removal
    try {
        Remove-Item -Path $path -Recurse -Force -ErrorAction Stop
        Write-Host "Removed: $path"
        return $true
    } catch {
        Write-Host "Failed to remove $path - Error: $($_.Exception.Message)"
        Write-Host "Attempting additional remedies: taskkill, takeown/icacls, then retry removal"
        # Try taskkill by image name (best-effort)
        try {
            $img = [System.IO.Path]::GetFileName($path)
            Write-Host "Running: taskkill /IM $img /F"
            Start-Process -FilePath "taskkill" -ArgumentList "/IM $img /F" -NoNewWindow -Wait -ErrorAction SilentlyContinue
            Start-Sleep -Milliseconds 200
        } catch {
            Write-Host "taskkill failed or not applicable - Error: $($_.Exception.Message)"
        }

        # Try to take ownership and grant full control
        try {
            Write-Host "Running: takeown /F `"$path`" /A"
            Start-Process -FilePath "takeown" -ArgumentList "/F `"$path`" /A" -NoNewWindow -Wait -ErrorAction SilentlyContinue
            Write-Host "Running: icacls `"$path`" /grant Everyone:F /C"
            Start-Process -FilePath "icacls" -ArgumentList "`"$path`" /grant Everyone:F /C" -NoNewWindow -Wait -ErrorAction SilentlyContinue
        } catch {
            Write-Host "takeown/icacls steps failed or require admin - Error: $($_.Exception.Message)"
        }

        # Retry removal once more
        try {
            Remove-Item -Path $path -Recurse -Force -ErrorAction Stop
            Write-Host "Removed after takeown/icacls: $path"
            return $true
        } catch {
            Write-Host "Final removal attempt failed - Error: $($_.Exception.Message)"
            return $false
        }
    }
}

if (Test-Path $distOnefile) {
    if (-not (Try-RemoveFile $distOnefile)) {
        Write-Host "WARNING: Unable to remove existing file: $distOnefile"
        Write-Host "Will continue and write to build-local dist to avoid permission issues."
    }
}
if (Test-Path $distOnedir) {
    if (-not (Try-RemoveFile $distOnedir)) {
        Write-Host "WARNING: Unable to remove existing folder: $distOnedir"
        Write-Host "Will continue and write to build-local dist to avoid permission issues."
    }
}

Write-Host "Running: pyinstaller $Spec (output appended to $log)"
# Use build-local dist and work paths to avoid conflicts with repo-level dist folder
$pyDist = Join-Path -Path $buildRoot -ChildPath "dist"
$pyWork = Join-Path -Path $buildRoot -ChildPath "work"
if (-not (Test-Path $pyDist)) { New-Item -ItemType Directory -Path $pyDist -Force | Out-Null }
if (-not (Test-Path $pyWork)) { New-Item -ItemType Directory -Path $pyWork -Force | Out-Null }

Write-Host "Running PyInstaller with distpath=$pyDist workpath=$pyWork"
& $Python -m PyInstaller $Spec --distpath "$pyDist" --workpath "$pyWork" 2>&1 | Tee-Object -FilePath $log

# Capture return code
$rc = $LASTEXITCODE
if ($rc -ne 0) {
    Write-Host "PyInstaller returned exit code $rc when using spec. See log: $log"
    Write-Host "Attempting fallback: pyinstaller --onefile --windowed main.py (appending to log)"
    Write-Host "Fallback will use distpath=$pyDist workpath=$pyWork and specpath=$buildRoot"
    & $Python -m PyInstaller --onefile --windowed --log-level=DEBUG --clean "main.py" --distpath "$pyDist" --workpath "$pyWork" --specpath "$buildRoot" 2>&1 | Tee-Object -FilePath $log -Append
    $rc = $LASTEXITCODE
}

# After PyInstaller run(s), check common output locations inside build-local dist.
$onefile = Join-Path -Path $pyDist -ChildPath "RMK_insGT.exe"
$onedir = Join-Path -Path $pyDist -ChildPath "RMK_insGT\RMK_insGT.exe"

if ($rc -ne 0) {
    Write-Host "PyInstaller failed with exit code $rc. Log saved to: $log"
    Write-Host "Please paste the contents of the log file when asking for help: $log"
    exit $rc
}

if (Test-Path $onefile) {
    $artifact = $onefile
} elseif (Test-Path $onedir) {
    $artifact = $onedir
} else {
    Write-Host "Build finished but no expected artifact was found."
    Write-Host "Checked: $onefile and $onedir"
    exit 2
}

# Ensure destination folder exists and copy artifact there for consistent output path
$destDir = Join-Path -Path $buildRoot -ChildPath "RMK_insGT"
if (-not (Test-Path $destDir)) {
    New-Item -ItemType Directory -Path $destDir -Force | Out-Null
}

Write-Host "Copying artifact to: $destDir"
Copy-Item -Path $artifact -Destination $destDir -Force

if ($?) {
    Write-Host "Build finished. Artifact copied to: $destDir"
    Write-Host "PyInstaller log: $log"
    exit 0
} else {
    Write-Host "Failed to copy artifact to: $destDir"
    Write-Host "PyInstaller log: $log"
    exit 3
}
