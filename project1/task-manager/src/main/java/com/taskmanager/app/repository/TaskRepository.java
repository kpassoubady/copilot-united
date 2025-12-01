package com.taskmanager.app.repository;

import com.taskmanager.app.entity.Task;
import com.taskmanager.app.entity.TaskStatus;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;
import java.util.List;

@Repository
public interface TaskRepository extends JpaRepository<Task, Long> {
    
    List<Task> findByStatus(TaskStatus status);
    
    // Students will expand this during exercises
}