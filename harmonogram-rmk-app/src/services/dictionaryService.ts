import { Account } from '../models/account';
import { RMK } from '../models/rmk';

class DictionaryService {
    private accounts: Account[] = [];

    addAccount(account: Account): void {
        this.accounts.push(account);
    }

    getAccounts(): Account[] {
        return this.accounts;
    }

    addDescriptionToAccount(accountId: string, description: string): void {
        const account = this.accounts.find(acc => acc.id === accountId);
        if (account) {
            account.description = description;
        }
    }
}

export default new DictionaryService();