export interface Account {
    id: number;
    name: string;
    description: string; // Added description field for the account
}

export class AccountModel {
    constructor(public account: Account) {}

    // Additional methods related to Account can be added here
}