document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('form');
    const taskTable = document.querySelector('table tbody');

    form.addEventListener('submit', function(event) {
        event.preventDefault();
        const formData = new FormData(form);
        const taskData = {};
        formData.forEach((value, key) => {
            taskData[key] = value;
        });

        fetch('/add_task', {
            method: 'POST',
            body: JSON.stringify(taskData),
            headers: {
                'Content-Type': 'application/json'
            }
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                addTaskToTable(taskData);
                form.reset();
            } else {
                alert('Error adding task');
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
    });

    function addTaskToTable(taskData) {
        const row = document.createElement('tr');
        Object.values(taskData).forEach(value => {
            const cell = document.createElement('td');
            cell.textContent = value;
            row.appendChild(cell);
        });
        taskTable.appendChild(row);
    }
});
