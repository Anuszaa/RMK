import { ReportsController } from '../src/controllers/reportsController';
import { RMK } from '../src/models/rmk';

describe('ReportsController', () => {
    let reportsController: ReportsController;

    beforeEach(() => {
        reportsController = new ReportsController();
    });

    it('should generate a report for all RMK entries', () => {
        const rmkEntries: RMK[] = [
            { id: 1, category: 'Category1', month: 'January', value: 100 },
            { id: 2, category: 'Category2', month: 'January', value: 200 },
            { id: 3, category: 'Category1', month: 'February', value: 150 },
        ];

        const report = reportsController.generateReport(rmkEntries);
        expect(report).toHaveProperty('total');
        expect(report.total).toBe(450);
    });

    it('should generate a monthly report for a specific category', () => {
        const rmkEntries: RMK[] = [
            { id: 1, category: 'Category1', month: 'January', value: 100 },
            { id: 2, category: 'Category1', month: 'January', value: 200 },
            { id: 3, category: 'Category2', month: 'January', value: 150 },
        ];

        const report = reportsController.generateMonthlyReport(rmkEntries, 'Category1', 'January');
        expect(report).toHaveProperty('total');
        expect(report.total).toBe(300);
    });

    it('should generate a report for a specific period', () => {
        const rmkEntries: RMK[] = [
            { id: 1, category: 'Category1', month: 'January', value: 100 },
            { id: 2, category: 'Category1', month: 'February', value: 200 },
            { id: 3, category: 'Category2', month: 'February', value: 150 },
        ];

        const report = reportsController.generatePeriodReport(rmkEntries, 'January', 'February');
        expect(report).toHaveProperty('total');
        expect(report.total).toBe(450);
    });
});