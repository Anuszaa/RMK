import { Request, Response } from 'express';
import { ReportsService } from '../services/reportsService';

export class ReportsController {
    private reportsService: ReportsService;

    constructor() {
        this.reportsService = new ReportsService();
    }

    public async getMonthlySummary(req: Request, res: Response): Promise<void> {
        const { month, category } = req.query;
        try {
            const summary = await this.reportsService.getMonthlySummary(month as string, category as string);
            res.status(200).json(summary);
        } catch (error) {
            res.status(500).json({ message: 'Error retrieving monthly summary', error });
        }
    }

    public async getCategorySummary(req: Request, res: Response): Promise<void> {
        const { category } = req.query;
        try {
            const summary = await this.reportsService.getCategorySummary(category as string);
            res.status(200).json(summary);
        } catch (error) {
            res.status(500).json({ message: 'Error retrieving category summary', error });
        }
    }

    public async getAllReports(req: Request, res: Response): Promise<void> {
        try {
            const reports = await this.reportsService.getAllReports();
            res.status(200).json(reports);
        } catch (error) {
            res.status(500).json({ message: 'Error retrieving reports', error });
        }
    }

    public async getReportsByPeriod(req: Request, res: Response): Promise<void> {
        const { startDate, endDate } = req.query;
        try {
            const reports = await this.reportsService.getReportsByPeriod(startDate as string, endDate as string);
            res.status(200).json(reports);
        } catch (error) {
            res.status(500).json({ message: 'Error retrieving reports by period', error });
        }
    }
}