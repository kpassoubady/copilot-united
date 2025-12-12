package com.taskmanager.app.controller;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

/**
 * Home controller responsible for rendering the application's landing page.
 * 
 * <p>This controller handles the root path ("/") and provides the main
 * entry point for users accessing the Task Manager application.</p>
 * 
 * @author Development Team
 * @version 1.0
 * @since 2025-12-12
 */
@Controller
public class HomeController {
    
    private static final Logger logger = LoggerFactory.getLogger(HomeController.class);
    private static final String VIEW_INDEX = "index";
    private static final String ATTR_MESSAGE = "message";
    
    @Value("${app.welcome.message:Welcome to Task Manager!}")
    private String welcomeMessage;
    
    /**
     * Displays the home page with a welcome message.
     * 
     * @param model the Spring MVC model to pass attributes to the view
     * @return the logical view name "index" which resolves to index.html/jsp
     */
    @GetMapping("/")
    public String home(Model model) {
        logger.debug("Home page accessed");
        model.addAttribute(ATTR_MESSAGE, welcomeMessage);
        return VIEW_INDEX;
    }
}