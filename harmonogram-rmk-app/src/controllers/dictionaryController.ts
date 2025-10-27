export class DictionaryController {
    private dictionaryService: any;

    constructor(dictionaryService: any) {
        this.dictionaryService = dictionaryService;
    }

    public async addAccount(req: any, res: any) {
        const { accountName, description } = req.body;

        try {
            const newAccount = await this.dictionaryService.addAccount(accountName, description);
            res.status(201).json(newAccount);
        } catch (error) {
            res.status(500).json({ message: error.message });
        }
    }

    public async getAccounts(req: any, res: any) {
        try {
            const accounts = await this.dictionaryService.getAccounts();
            res.status(200).json(accounts);
        } catch (error) {
            res.status(500).json({ message: error.message });
        }
    }
}