document.addEventListener("DOMContentLoaded", function () {
    loadTasks();
});

function addTask() {
    let taskInput = document.getElementById("taskInput");
    let taskText = taskInput.value.trim();

    if (taskText === "") return;

    let taskList = document.getElementById("taskList");

    let li = document.createElement("li");
    li.innerHTML = `
        <div class="task-container">
            <input type="checkbox" class="checkbox" onclick="toggleTask(this)">
            <span class="task-text">${taskText}</span>
        </div>
        <button class="delete-btn" onclick="deleteTask(this)">🗑</button>
    `;

    taskList.appendChild(li);
    saveTasks();

    taskInput.value = "";
}

function toggleTask(checkbox) {
    let taskText = checkbox.nextElementSibling;
    if (checkbox.checked) {
        taskText.classList.add("completed");
    } else {
        taskText.classList.remove("completed");
    }
    saveTasks();
}

function deleteTask(button) {
    button.parentElement.remove();
    saveTasks();
}

function saveTasks() {
    let tasks = [];
    document.querySelectorAll("#taskList li").forEach(li => {
        let text = li.querySelector(".task-text").textContent;
        let completed = li.querySelector(".checkbox").checked;
        tasks.push({ text, completed });
    });
    localStorage.setItem("tasks", JSON.stringify(tasks));
}

function loadTasks() {
    let storedTasks = localStorage.getItem("tasks");
    if (storedTasks) {
        let tasks = JSON.parse(storedTasks);
        let taskList = document.getElementById("taskList");

        tasks.forEach(task => {
            let li = document.createElement("li");
            li.innerHTML = `
                <div class="task-container">
                    <input type="checkbox" class="checkbox" onclick="toggleTask(this)" ${task.completed ? "checked" : ""}>
                    <span class="task-text ${task.completed ? "completed" : ""}">${task.text}</span>
                </div>
                <button class="delete-btn" onclick="deleteTask(this)">🗑</button>
            `;
            taskList.appendChild(li);
        });
    }
}