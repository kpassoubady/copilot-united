package com.taskmanager.app.service;

import org.springframework.stereotype.Service;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

@Service
public class EmailService {
    
    private static final Logger logger = LoggerFactory.getLogger(EmailService.class);
    
    public void sendWelcomeEmail(String email) {
        // Stub implementation for training
        logger.info("Welcome email would be sent to: {}", email);
    }
    
    public void sendTaskAssignmentEmail(String email, String taskTitle) {
        logger.info("Task assignment email for '{}' would be sent to: {}", taskTitle, email);
    }
    
    // Students will expand this during exercises
}
