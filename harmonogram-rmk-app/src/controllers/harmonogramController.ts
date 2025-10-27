import { Request, Response } from 'express';
import { HarmonogramService } from '../services/harmonogramService';
import { ReportsService } from '../services/reportsService';

export class HarmonogramController {
    private harmonogramService: HarmonogramService;
    private reportsService: ReportsService;

    constructor() {
        this.harmonogramService = new HarmonogramService();
        this.reportsService = new ReportsService();
    }

    public async getHarmonogram(req: Request, res: Response): Promise<void> {
        try {
            const harmonogram = await this.harmonogramService.getHarmonogram();
            res.json(harmonogram);
        } catch (error) {
            res.status(500).json({ message: 'Error retrieving harmonogram', error });
        }
    }

    public async getAggregatedRMKByCategory(req: Request, res: Response): Promise<void> {
        try {
            const aggregatedData = await this.harmonogramService.getAggregatedRMKByCategory();
            res.json(aggregatedData);
        } catch (error) {
            res.status(500).json({ message: 'Error retrieving aggregated RMK data', error });
        }
    }

    public async getAggregatedRMKByMonth(req: Request, res: Response): Promise<void> {
        try {
            const aggregatedData = await this.harmonogramService.getAggregatedRMKByMonth();
            res.json(aggregatedData);
        } catch (error) {
            res.status(500).json({ message: 'Error retrieving aggregated RMK data by month', error });
        }
    }
}