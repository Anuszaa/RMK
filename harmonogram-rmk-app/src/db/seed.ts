import { Account } from '../models/account';
import { RMK } from '../models/rmk';

const seedData = async () => {
    const accounts: Account[] = [
        { id: 1, name: 'Account 1', description: 'Description for Account 1' },
        { id: 2, name: 'Account 2', description: 'Description for Account 2' },
        { id: 3, name: 'Account 3', description: 'Description for Account 3' },
    ];

    const rmkEntries: RMK[] = [
        { id: 1, title: 'RMK Entry 1', category: 'Category A', date: new Date('2023-01-15') },
        { id: 2, title: 'RMK Entry 2', category: 'Category B', date: new Date('2023-02-20') },
        { id: 3, title: 'RMK Entry 3', category: 'Category A', date: new Date('2023-03-10') },
    ];

    // Assuming you have a database connection and models set up
    await Account.insertMany(accounts);
    await RMK.insertMany(rmkEntries);
};

seedData().catch(error => {
    console.error('Error seeding data:', error);
});