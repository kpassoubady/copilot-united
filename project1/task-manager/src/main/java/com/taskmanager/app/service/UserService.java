package com.taskmanager.app.service;

import com.taskmanager.app.repository.UserRepository;
import org.springframework.stereotype.Service;

@Service
public class UserService {
    
    // Foundation fields available for Copilot exercises
    private final UserRepository userRepository;
    private final PasswordEncoder passwordEncoder;
    private final EmailService emailService;
    
    public UserService(UserRepository userRepository, PasswordEncoder passwordEncoder, EmailService emailService) {
        this.userRepository = userRepository;
        this.passwordEncoder = passwordEncoder;
        this.emailService = emailService;
    }
    
    // Students will add methods during exercises with Copilot assistance
    
}