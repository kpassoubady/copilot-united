using TaskManager.Web.DTOs;

namespace TaskManager.Web.Services;

/// <summary>
/// Service interface for category operations.
/// </summary>
public interface ICategoryService
{
    /// <summary>
    /// Gets all categories.
    /// </summary>
    Task<IEnumerable<CategoryDto>> GetAllCategoriesAsync();

    /// <summary>
    /// Gets a category by its ID.
    /// </summary>
    Task<CategoryDto?> GetCategoryByIdAsync(Guid id);

    /// <summary>
    /// Creates a new category.
    /// </summary>
    Task<CategoryDto> CreateCategoryAsync(CreateCategoryDto createDto);

    /// <summary>
    /// Updates an existing category.
    /// </summary>
    Task<CategoryDto?> UpdateCategoryAsync(Guid id, UpdateCategoryDto updateDto);

    /// <summary>
    /// Deletes a category.
    /// </summary>
    Task<bool> DeleteCategoryAsync(Guid id);

    /// <summary>
    /// Gets categories with task counts.
    /// </summary>
    Task<IEnumerable<CategoryWithTaskCountDto>> GetCategoriesWithTaskCountsAsync();
}
