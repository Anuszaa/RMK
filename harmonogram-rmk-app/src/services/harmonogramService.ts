import { RMK } from '../models/rmk';
import { Account } from '../models/account';

class HarmonogramService {
    private rmkData: RMK[] = [];
    private accounts: Account[] = [];

    constructor(rmkData: RMK[], accounts: Account[]) {
        this.rmkData = rmkData;
        this.accounts = accounts;
    }

    public generateSchedule(): any {
        // Logic to generate the schedule based on RMK data
    }

    public aggregateRMKByCategory(): any {
        // Logic to aggregate RMK data by category
    }

    public aggregateRMKByMonth(): any {
        // Logic to aggregate RMK data by month
    }

    public getTotalRMKByCategory(): any {
        // Logic to get total RMK entries by category
    }

    public getTotalRMKByMonth(): any {
        // Logic to get total RMK entries by month
    }
}

export default HarmonogramService;