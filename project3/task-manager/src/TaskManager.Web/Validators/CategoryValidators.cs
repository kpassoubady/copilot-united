using FluentValidation;
using TaskManager.Web.DTOs;

namespace TaskManager.Web.Validators;

/// <summary>
/// Validator for CreateCategoryDto.
/// </summary>
public class CreateCategoryDtoValidator : AbstractValidator<CreateCategoryDto>
{
    public CreateCategoryDtoValidator()
    {
        RuleFor(x => x.Name)
            .NotEmpty().WithMessage("Category name is required")
            .MaximumLength(100).WithMessage("Category name cannot exceed 100 characters");

        RuleFor(x => x.Description)
            .MaximumLength(255).WithMessage("Description cannot exceed 255 characters");

        RuleFor(x => x.Icon)
            .MaximumLength(50).WithMessage("Icon cannot exceed 50 characters");

        RuleFor(x => x.Color)
            .Matches(@"^#[0-9A-Fa-f]{6}$")
            .When(x => !string.IsNullOrEmpty(x.Color))
            .WithMessage("Color must be a valid hex color code (e.g., #FF5733)");
    }
}

/// <summary>
/// Validator for UpdateCategoryDto.
/// </summary>
public class UpdateCategoryDtoValidator : AbstractValidator<UpdateCategoryDto>
{
    public UpdateCategoryDtoValidator()
    {
        RuleFor(x => x.Name)
            .MaximumLength(100).WithMessage("Category name cannot exceed 100 characters")
            .When(x => x.Name != null);

        RuleFor(x => x.Description)
            .MaximumLength(255).WithMessage("Description cannot exceed 255 characters")
            .When(x => x.Description != null);

        RuleFor(x => x.Icon)
            .MaximumLength(50).WithMessage("Icon cannot exceed 50 characters")
            .When(x => x.Icon != null);

        RuleFor(x => x.Color)
            .Matches(@"^#[0-9A-Fa-f]{6}$")
            .When(x => !string.IsNullOrEmpty(x.Color))
            .WithMessage("Color must be a valid hex color code (e.g., #FF5733)");
    }
}
