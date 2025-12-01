package com.taskmanager.app.service;

import com.taskmanager.app.repository.TaskRepository;
import org.springframework.stereotype.Service;

@Service
public class TaskService {

    private final TaskRepository taskRepository;
    
    public TaskService(TaskRepository taskRepository) {
        this.taskRepository = taskRepository;
    }
    
    // Practice area - type the comment and method signature slowly
    // Create a method to update task status
    public void updateTaskStatus(Long taskId, String status) {
        // Implementation goes here
    }

    // Create a method to validate task data
public boolean validateTaskData(Long taskId, String status) {
    // Implementation goes here
    return true;    

}
}