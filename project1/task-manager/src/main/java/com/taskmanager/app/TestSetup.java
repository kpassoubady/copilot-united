package com.taskmanager.app;

import com.taskmanager.app.entity.User;
import com.taskmanager.app.entity.Task;
import com.taskmanager.app.dto.CreateUserRequest;

public class TestSetup {
    public static void main(String[] args) {
        System.out.println("✅ All foundation classes are available!");
        System.out.println("✅ Ready for Copilot exercises!");
        
        // If this compiles without errors, you're ready to start
        User user = new User("John", "Doe", "john@example.com");
        Task task = new Task();
        CreateUserRequest request = new CreateUserRequest();
        
        System.out.println("Foundation setup verification complete!");
    }
}