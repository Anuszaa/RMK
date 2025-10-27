import React, { useEffect, useState } from 'react';
import { fetchHarmonogramData } from '../../services/harmonogramService';
import { RMKEntry } from '../../models/rmk';

const Harmonogram: React.FC = () => {
    const [rmkEntries, setRmkEntries] = useState<RMKEntry[]>([]);
    const [loading, setLoading] = useState<boolean>(true);

    useEffect(() => {
        const loadData = async () => {
            const data = await fetchHarmonogramData();
            setRmkEntries(data);
            setLoading(false);
        };

        loadData();
    }, []);

    const renderEntries = () => {
        return rmkEntries.map((entry) => (
            <div key={entry.id}>
                <h3>{entry.title}</h3>
                <p>{entry.description}</p>
                <p>Category: {entry.category}</p>
                <p>Date: {entry.date}</p>
            </div>
        ));
    };

    if (loading) {
        return <div>Loading...</div>;
    }

    return (
        <div>
            <h1>Harmonogram RMK</h1>
            {renderEntries()}
        </div>
    );
};

export default Harmonogram;