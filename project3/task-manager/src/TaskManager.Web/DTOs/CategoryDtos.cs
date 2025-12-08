namespace TaskManager.Web.DTOs;

/// <summary>
/// DTO for category display.
/// </summary>
public record CategoryDto
{
    public Guid Id { get; init; }
    public string Name { get; init; } = string.Empty;
    public string? Description { get; init; }
    public string? Icon { get; init; }
    public string Color { get; init; } = "#6c757d";
    public DateTime CreatedAt { get; init; }
    public DateTime UpdatedAt { get; init; }
}

/// <summary>
/// DTO for creating a new category.
/// </summary>
public record CreateCategoryDto
{
    public string Name { get; init; } = string.Empty;
    public string? Description { get; init; }
    public string? Icon { get; init; }
    public string? Color { get; init; }
}

/// <summary>
/// DTO for updating an existing category.
/// </summary>
public record UpdateCategoryDto
{
    public string? Name { get; init; }
    public string? Description { get; init; }
    public string? Icon { get; init; }
    public string? Color { get; init; }
}

/// <summary>
/// DTO for category with task count.
/// </summary>
public record CategoryWithTaskCountDto
{
    public Guid Id { get; init; }
    public string Name { get; init; } = string.Empty;
    public string? Description { get; init; }
    public string? Icon { get; init; }
    public string Color { get; init; } = "#6c757d";
    public int TotalTasks { get; init; }
    public int ActiveTasks { get; init; }
    public int CompletedTasks { get; init; }
}
