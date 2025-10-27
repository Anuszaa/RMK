import { Account } from '../src/models/account';
import { DictionaryService } from '../src/services/dictionaryService';

describe('Dictionary Service', () => {
    let dictionaryService: DictionaryService;

    beforeEach(() => {
        dictionaryService = new DictionaryService();
    });

    it('should add an account with a description', () => {
        const account: Account = {
            id: '1',
            name: 'Test Account',
            description: 'This is a test account description'
        };

        dictionaryService.addAccount(account);
        const accounts = dictionaryService.getAccounts();

        expect(accounts).toContainEqual(account);
    });

    it('should not add an account without a name', () => {
        const account: Account = {
            id: '2',
            name: '',
            description: 'This account has no name'
        };

        dictionaryService.addAccount(account);
        const accounts = dictionaryService.getAccounts();

        expect(accounts).not.toContainEqual(account);
    });

    it('should retrieve accounts with descriptions', () => {
        const account1: Account = {
            id: '3',
            name: 'Account 1',
            description: 'Description for account 1'
        };

        const account2: Account = {
            id: '4',
            name: 'Account 2',
            description: 'Description for account 2'
        };

        dictionaryService.addAccount(account1);
        dictionaryService.addAccount(account2);
        const accounts = dictionaryService.getAccounts();

        expect(accounts).toEqual(expect.arrayContaining([account1, account2]));
    });
});