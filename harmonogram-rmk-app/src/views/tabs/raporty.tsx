import React, { useEffect, useState } from 'react';
import { fetchReports } from '../../services/reportsService';
import { RMKSummary } from '../components/rmk-summary';

const Raporty = () => {
    const [reports, setReports] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        const loadReports = async () => {
            try {
                const data = await fetchReports();
                setReports(data);
            } catch (err) {
                setError(err.message);
            } finally {
                setLoading(false);
            }
        };

        loadReports();
    }, []);

    if (loading) {
        return <div>Loading...</div>;
    }

    if (error) {
        return <div>Error: {error}</div>;
    }

    const groupedByMonth = reports.reduce((acc, report) => {
        const month = new Date(report.date).toLocaleString('default', { month: 'long' });
        if (!acc[month]) {
            acc[month] = [];
        }
        acc[month].push(report);
        return acc;
    }, {});

    return (
        <div>
            <h1>Raporty RMK</h1>
            {Object.keys(groupedByMonth).map(month => (
                <div key={month}>
                    <h2>{month}</h2>
                    {groupedByMonth[month].map(report => (
                        <RMKSummary key={report.id} report={report} />
                    ))}
                </div>
            ))}
        </div>
    );
};

export default Raporty;