package com.taskmanager.app.service;

import org.springframework.stereotype.Component;
import java.util.Base64;

@Component
public class PasswordEncoder {
    
    /**
     * Simple encoding for training purposes only
     * In production, use BCryptPasswordEncoder or similar
     */
    public String encode(String rawPassword) {
        return Base64.getEncoder().encodeToString(rawPassword.getBytes());
    }
    
    public boolean matches(String rawPassword, String encodedPassword) {
        return encode(rawPassword).equals(encodedPassword);
    }
}