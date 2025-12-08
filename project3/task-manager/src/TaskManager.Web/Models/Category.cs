using System.ComponentModel.DataAnnotations;

namespace TaskManager.Web.Models;

/// <summary>
/// Represents a category for organizing tasks.
/// </summary>
public class Category
{
    [Key]
    public Guid Id { get; set; } = Guid.NewGuid();

    [Required]
    [MaxLength(100)]
    public string Name { get; set; } = string.Empty;

    [MaxLength(255)]
    public string? Description { get; set; }

    [MaxLength(50)]
    public string? Icon { get; set; }

    [MaxLength(7)]
    [RegularExpression(@"^#[0-9A-Fa-f]{6}$", ErrorMessage = "Color must be a valid hex color code (e.g., #FF5733)")]
    public string Color { get; set; } = "#6c757d";

    public DateTime CreatedAt { get; set; } = DateTime.UtcNow;
    public DateTime UpdatedAt { get; set; } = DateTime.UtcNow;

    // Navigation property
    public ICollection<TaskItem> Tasks { get; set; } = new List<TaskItem>();

    public Category()
    {
    }

    public Category(string name, string? description = null, string? icon = null, string? color = null)
    {
        Name = name;
        Description = description;
        Icon = icon;
        Color = color ?? "#6c757d";
    }

    /// <summary>
    /// Gets the count of active (non-completed) tasks in this category.
    /// </summary>
    public int ActiveTaskCount => Tasks.Count(t => t.Status != TaskStatus.Done && t.Status != TaskStatus.Cancelled);
}
