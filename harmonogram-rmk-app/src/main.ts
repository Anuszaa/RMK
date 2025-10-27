import express from 'express';
import bodyParser from 'body-parser';
import { createConnection } from 'typeorm';
import { routes } from './routes/index';

const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

// Database connection
createConnection()
    .then(() => {
        console.log('Database connected successfully');
        
        // Routes
        app.use('/api', routes);

        // Start server
        app.listen(PORT, () => {
            console.log(`Server is running on http://localhost:${PORT}`);
        });
    })
    .catch(error => console.log('Database connection error:', error));