package com.taskmanager.app;

import com.taskmanager.app.entity.User;
import com.taskmanager.app.entity.Task;
import com.taskmanager.app.entity.TaskStatus;
import com.taskmanager.app.repository.UserRepository;
import com.taskmanager.app.repository.TaskRepository;
import com.taskmanager.app.service.UserService;
import com.taskmanager.app.service.TaskService;
import com.taskmanager.app.service.EmailService;
import com.taskmanager.app.service.PasswordEncoder;
import com.taskmanager.app.dto.CreateUserRequest;
import com.taskmanager.app.exception.UserNotFoundException;
import com.taskmanager.app.exception.UserAlreadyExistsException;
import com.taskmanager.app.exception.ValidationException;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.DisplayName;
import static org.junit.jupiter.api.Assertions.*;

/**
 * Foundation Classes Validation Test
 * 
 * This test validates that all foundational classes are properly structured
 * and available for GitHub Copilot exercises. It serves as a setup verification
 * for instructors before beginning hands-on training sessions.
 */
public class FoundationClassesTest {

    @Test
    @DisplayName("Verify all entity classes exist and can be instantiated")
    public void testEntityClasses() {
        assertDoesNotThrow(() -> {
            User user = new User();
            assertNotNull(user);
            
            Task task = new Task();
            assertNotNull(task);
            
            TaskStatus status = TaskStatus.PENDING;
            assertNotNull(status);
        }, "All entity classes should be instantiable");
    }

    @Test
    @DisplayName("Verify all repository interfaces exist")
    public void testRepositoryInterfaces() {
        assertDoesNotThrow(() -> {
            Class<?> userRepoClass = UserRepository.class;
            Class<?> taskRepoClass = TaskRepository.class;
            
            assertNotNull(userRepoClass);
            assertNotNull(taskRepoClass);
            assertTrue(userRepoClass.isInterface());
            assertTrue(taskRepoClass.isInterface());
        }, "Repository interfaces should exist and be interfaces");
    }

    @Test
    @DisplayName("Verify all service classes exist")
    public void testServiceClasses() {
        assertDoesNotThrow(() -> {
            Class<?> userServiceClass = UserService.class;
            Class<?> taskServiceClass = TaskService.class;
            Class<?> emailServiceClass = EmailService.class;
            Class<?> passwordEncoderClass = PasswordEncoder.class;
            
            assertNotNull(userServiceClass);
            assertNotNull(taskServiceClass);
            assertNotNull(emailServiceClass);
            assertNotNull(passwordEncoderClass);
        }, "All service classes should exist");
    }

    @Test
    @DisplayName("Verify all DTO classes exist")
    public void testDtoClasses() {
        assertDoesNotThrow(() -> {
            CreateUserRequest dto = new CreateUserRequest();
            assertNotNull(dto);
        }, "DTO classes should be instantiable");
    }

    @Test
    @DisplayName("Verify all exception classes exist")
    public void testExceptionClasses() {
        assertDoesNotThrow(() -> {
            Class<?> userNotFoundClass = UserNotFoundException.class;
            Class<?> userExistsClass = UserAlreadyExistsException.class;
            Class<?> validationClass = ValidationException.class;
            
            assertNotNull(userNotFoundClass);
            assertNotNull(userExistsClass);
            assertNotNull(validationClass);
            
            // Verify they extend appropriate base classes
            assertTrue(RuntimeException.class.isAssignableFrom(userNotFoundClass));
            assertTrue(RuntimeException.class.isAssignableFrom(userExistsClass));
            assertTrue(RuntimeException.class.isAssignableFrom(validationClass));
        }, "Exception classes should exist and extend RuntimeException");
    }

    @Test
    @DisplayName("Verify package structure is correct")
    public void testPackageStructure() {
        assertEquals("com.taskmanager.app.entity", User.class.getPackageName());
        assertEquals("com.taskmanager.app.entity", Task.class.getPackageName());
        assertEquals("com.taskmanager.app.entity", TaskStatus.class.getPackageName());
        assertEquals("com.taskmanager.app.repository", UserRepository.class.getPackageName());
        assertEquals("com.taskmanager.app.repository", TaskRepository.class.getPackageName());
        assertEquals("com.taskmanager.app.service", UserService.class.getPackageName());
        assertEquals("com.taskmanager.app.service", TaskService.class.getPackageName());
        assertEquals("com.taskmanager.app.dto", CreateUserRequest.class.getPackageName());
        assertEquals("com.taskmanager.app.exception", UserNotFoundException.class.getPackageName());
    }

}