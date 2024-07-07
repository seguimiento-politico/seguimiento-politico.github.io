// DEPRECATED
const fs = require('fs');

const filePath = process.argv[2];

if (!filePath) {
    console.error('Usage: node insertUuid.js <path-to-yaml-file>');
    process.exit(1);
}

fs.readFile(filePath, 'utf8', (err, data) => {
    if (err) {
        console.error(err);
        process.exit(1);
    }

    const lines = data.split('\n');
    for (let i = 0; i < lines.length; i++) {
        if (lines[i].includes('chapter:')) {
            const newUuid = generateUuid();
            lines.splice(i + 1, 0, `  id: ${newUuid}`);
            i++; // Skip the next line (uuid line) in the next iteration
        }
    }

    const updatedData = lines.join('\n');
    fs.writeFile(filePath, updatedData, 'utf8', (err) => {
        if (err) {
            console.error(err);
            process.exit(1);
        }
        console.log('UUIDs inserted successfully!');
    });
});

function generateUuid() {
    return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function (c) {
        const r = (Math.random() * 16) | 0;
        const v = c === 'x' ? r : (r & 0x3) | 0x8;
        return v.toString(16);
    });
}
