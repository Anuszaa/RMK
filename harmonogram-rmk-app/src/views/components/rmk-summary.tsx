import React from 'react';
import { RMK } from '../../models/rmk';

interface RMKSummaryProps {
    rmkData: RMK[];
}

const RMKSummary: React.FC<RMKSummaryProps> = ({ rmkData }) => {
    const categories = Array.from(new Set(rmkData.map(item => item.category)));
    
    const summaryByCategory = categories.map(category => {
        const total = rmkData.filter(item => item.category === category).reduce((acc, item) => acc + item.amount, 0);
        return { category, total };
    });

    return (
        <div>
            <h2>RMK Summary</h2>
            <table>
                <thead>
                    <tr>
                        <th>Category</th>
                        <th>Total</th>
                    </tr>
                </thead>
                <tbody>
                    {summaryByCategory.map((summary, index) => (
                        <tr key={index}>
                            <td>{summary.category}</td>
                            <td>{summary.total}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
};

export default RMKSummary;