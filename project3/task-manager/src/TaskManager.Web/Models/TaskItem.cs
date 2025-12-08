using System.ComponentModel.DataAnnotations;

namespace TaskManager.Web.Models;

/// <summary>
/// Represents a task item in the task manager application.
/// </summary>
public class TaskItem
{
    [Key]
    public Guid Id { get; set; } = Guid.NewGuid();

    [Required]
    [MaxLength(200)]
    public string Title { get; set; } = string.Empty;

    [MaxLength(1000)]
    public string? Description { get; set; }

    [Required]
    public TaskPriority Priority { get; set; } = TaskPriority.Medium;

    [Required]
    public TaskStatus Status { get; set; } = TaskStatus.Todo;

    public DateTime? DueDate { get; set; }

    public DateTime? CompletedAt { get; set; }

    [Required]
    public Guid CategoryId { get; set; }

    // Navigation property
    public Category Category { get; set; } = null!;

    public DateTime CreatedAt { get; set; } = DateTime.UtcNow;
    public DateTime UpdatedAt { get; set; } = DateTime.UtcNow;

    public TaskItem()
    {
    }

    public TaskItem(string title, string? description, TaskPriority priority, Guid categoryId, DateTime? dueDate = null)
    {
        Title = title;
        Description = description;
        Priority = priority;
        CategoryId = categoryId;
        DueDate = dueDate;
    }

    /// <summary>
    /// Marks the task as complete.
    /// </summary>
    public void MarkComplete()
    {
        Status = TaskStatus.Done;
        CompletedAt = DateTime.UtcNow;
    }

    /// <summary>
    /// Determines if the task is overdue.
    /// </summary>
    public bool IsOverdue => DueDate.HasValue && DueDate.Value < DateTime.Today && Status != TaskStatus.Done;
}

/// <summary>
/// Task priority levels.
/// </summary>
public enum TaskPriority
{
    Low = 0,
    Medium = 1,
    High = 2,
    Critical = 3
}

/// <summary>
/// Task status values.
/// </summary>
public enum TaskStatus
{
    Todo = 0,
    InProgress = 1,
    Done = 2,
    Cancelled = 3
}
