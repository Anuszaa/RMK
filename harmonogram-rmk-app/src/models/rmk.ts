export interface RMK {
    id: number;
    name: string;
    category: string;
    description: string; // Added description field
    date: Date;
    amount: number;
}

export class RMKModel {
    private rmkEntries: RMK[] = [];

    addEntry(entry: RMK): void {
        this.rmkEntries.push(entry);
    }

    getEntriesByCategory(category: string): RMK[] {
        return this.rmkEntries.filter(entry => entry.category === category);
    }

    getEntriesByMonth(month: number, year: number): RMK[] {
        return this.rmkEntries.filter(entry => {
            const entryDate = new Date(entry.date);
            return entryDate.getMonth() === month && entryDate.getFullYear() === year;
        });
    }

    getAllEntries(): RMK[] {
        return this.rmkEntries;
    }
}