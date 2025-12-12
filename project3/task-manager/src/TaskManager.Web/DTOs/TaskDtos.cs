using TaskManager.Web.Models;

namespace TaskManager.Web.DTOs;

/// <summary>
/// DTO for task item display.
/// </summary>
public record TaskItemDto
{
    public Guid Id { get; init; }
    public string Title { get; init; } = string.Empty;
    public string? Description { get; init; }
    public TaskPriority Priority { get; init; }
    public Models.TaskStatus Status { get; init; }
    public DateTime? DueDate { get; init; }
    public DateTime? CompletedAt { get; init; }
    public Guid CategoryId { get; init; }
    public string CategoryName { get; init; } = string.Empty;
    public string CategoryColor { get; init; } = "#6c757d";
    public DateTime CreatedAt { get; init; }
    public DateTime UpdatedAt { get; init; }
    public bool IsOverdue { get; init; }
}

/// <summary>
/// DTO for creating a new task.
/// </summary>
public record CreateTaskDto
{
    public string Title { get; init; } = string.Empty;
    public string? Description { get; init; }
    public TaskPriority Priority { get; init; } = TaskPriority.Medium;
    public Guid CategoryId { get; init; }
    public DateTime? DueDate { get; init; }
}

/// <summary>
/// DTO for updating an existing task.
/// </summary>
public record UpdateTaskDto
{
    public string? Title { get; init; }
    public string? Description { get; init; }
    public TaskPriority? Priority { get; init; }
    public Models.TaskStatus? Status { get; init; }
    public Guid? CategoryId { get; init; }
    public DateTime? DueDate { get; init; }
}

/// <summary>
/// DTO for filtering tasks.
/// </summary>
public record TaskFilterDto
{
    public Models.TaskStatus? Status { get; init; }
    public TaskPriority? Priority { get; init; }
    public Guid? CategoryId { get; init; }
    public bool? IsOverdue { get; init; }
    public DateTime? DueDateFrom { get; init; }
    public DateTime? DueDateTo { get; init; }
    public string? SearchTerm { get; init; }
}

/// <summary>
/// DTO for task statistics.
/// </summary>
public record TaskStatisticsDto
{
    public int TotalTasks { get; init; }
    public int TodoTasks { get; init; }
    public int InProgressTasks { get; init; }
    public int CompletedTasks { get; init; }
    public int OverdueTasks { get; init; }
    public int TasksDueToday { get; init; }
    public int TasksDueThisWeek { get; init; }
    public Dictionary<string, int> TasksByCategory { get; init; } = new();
    public Dictionary<string, int> TasksByPriority { get; init; } = new();
}
