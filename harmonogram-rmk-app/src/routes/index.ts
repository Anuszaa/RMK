import { Router } from 'express';
import DictionaryController from '../controllers/dictionaryController';
import HarmonogramController from '../controllers/harmonogramController';
import ReportsController from '../controllers/reportsController';

const router = Router();

const dictionaryController = new DictionaryController();
const harmonogramController = new HarmonogramController();
const reportsController = new ReportsController();

// Routes for dictionary operations
router.post('/accounts', dictionaryController.addAccountWithDescription);
router.get('/accounts', dictionaryController.getAccounts);

// Routes for harmonogram operations
router.get('/harmonogram', harmonogramController.getHarmonogram);
router.get('/harmonogram/summary', harmonogramController.getSummaryByCategoryAndMonth);

// Routes for reports
router.get('/reports', reportsController.getReports);
router.get('/reports/category/:category', reportsController.getReportsByCategory);
router.get('/reports/month/:month', reportsController.getReportsByMonth);
router.get('/reports/period', reportsController.getReportsByPeriod);

export default router;