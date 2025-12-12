using TaskManager.Web.DTOs;
using TaskManager.Web.Models;

namespace TaskManager.Web.Services;

/// <summary>
/// Service interface for task operations.
/// </summary>
public interface ITaskService
{
    /// <summary>
    /// Gets all tasks with optional filtering.
    /// </summary>
    Task<IEnumerable<TaskItemDto>> GetAllTasksAsync(TaskFilterDto? filter = null);

    /// <summary>
    /// Gets a task by its ID.
    /// </summary>
    Task<TaskItemDto?> GetTaskByIdAsync(Guid id);

    /// <summary>
    /// Creates a new task.
    /// </summary>
    Task<TaskItemDto> CreateTaskAsync(CreateTaskDto createDto);

    /// <summary>
    /// Updates an existing task.
    /// </summary>
    Task<TaskItemDto?> UpdateTaskAsync(Guid id, UpdateTaskDto updateDto);

    /// <summary>
    /// Deletes a task.
    /// </summary>
    Task<bool> DeleteTaskAsync(Guid id);

    /// <summary>
    /// Marks a task as complete.
    /// </summary>
    Task<TaskItemDto?> CompleteTaskAsync(Guid id);

    /// <summary>
    /// Gets tasks by category.
    /// </summary>
    Task<IEnumerable<TaskItemDto>> GetTasksByCategoryAsync(Guid categoryId);

    /// <summary>
    /// Gets overdue tasks.
    /// </summary>
    Task<IEnumerable<TaskItemDto>> GetOverdueTasksAsync();

    /// <summary>
    /// Gets task statistics.
    /// </summary>
    Task<TaskStatisticsDto> GetTaskStatisticsAsync();
}
