import { RMK } from '../models/rmk';
import { Account } from '../models/account';

export class ReportsService {
    private rmkData: RMK[];
    private accounts: Account[];

    constructor(rmkData: RMK[], accounts: Account[]) {
        this.rmkData = rmkData;
        this.accounts = accounts;
    }

    public getMonthlySummary(month: number, year: number) {
        const monthlySummary = this.rmkData
            .filter(rmk => new Date(rmk.date).getMonth() === month && new Date(rmk.date).getFullYear() === year)
            .reduce((summary, rmk) => {
                const category = rmk.category;
                if (!summary[category]) {
                    summary[category] = 0;
                }
                summary[category] += rmk.amount;
                return summary;
            }, {} as Record<string, number>);

        return monthlySummary;
    }

    public getCategorySummary(category: string) {
        const categorySummary = this.rmkData
            .filter(rmk => rmk.category === category)
            .reduce((total, rmk) => total + rmk.amount, 0);

        return categorySummary;
    }

    public getOverallSummary() {
        return this.rmkData.reduce((total, rmk) => total + rmk.amount, 0);
    }

    public getReportsByPeriod(startDate: Date, endDate: Date) {
        return this.rmkData
            .filter(rmk => new Date(rmk.date) >= startDate && new Date(rmk.date) <= endDate)
            .reduce((summary, rmk) => {
                const category = rmk.category;
                if (!summary[category]) {
                    summary[category] = 0;
                }
                summary[category] += rmk.amount;
                return summary;
            }, {} as Record<string, number>);
    }
}