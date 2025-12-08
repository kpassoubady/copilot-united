using Microsoft.EntityFrameworkCore;
using TaskManager.Web.Models;

namespace TaskManager.Web.Data;

/// <summary>
/// Entity Framework Core database context for the Task Manager application.
/// </summary>
public class TaskManagerContext : DbContext
{
    public TaskManagerContext(DbContextOptions<TaskManagerContext> options)
        : base(options)
    {
    }

    public DbSet<TaskItem> Tasks => Set<TaskItem>();
    public DbSet<Category> Categories => Set<Category>();

    protected override void OnModelCreating(ModelBuilder modelBuilder)
    {
        base.OnModelCreating(modelBuilder);

        // Category configuration
        modelBuilder.Entity<Category>(entity =>
        {
            entity.HasIndex(c => c.Name).IsUnique();
            entity.Property(c => c.Color).HasDefaultValue("#6c757d");
        });

        // TaskItem configuration
        modelBuilder.Entity<TaskItem>(entity =>
        {
            entity.HasOne(t => t.Category)
                  .WithMany(c => c.Tasks)
                  .HasForeignKey(t => t.CategoryId)
                  .OnDelete(DeleteBehavior.Cascade);

            entity.HasIndex(t => t.Status);
            entity.HasIndex(t => t.DueDate);
        });

        // Seed data
        SeedData(modelBuilder);
    }

    private void SeedData(ModelBuilder modelBuilder)
    {
        // Use fixed values for reproducible migrations
        var fixedDate = new DateTime(2024, 1, 1, 0, 0, 0, DateTimeKind.Utc);
        
        modelBuilder.Entity<Category>().HasData(
            new { Id = Guid.Parse("a1b2c3d4-e5f6-7890-abcd-ef1234567890"), Name = "Work", Icon = "fas fa-briefcase", Color = "#FF6384", Description = "Work-related tasks", CreatedAt = fixedDate, UpdatedAt = fixedDate },
            new { Id = Guid.Parse("b2c3d4e5-f6a7-8901-bcde-f12345678901"), Name = "Personal", Icon = "fas fa-user", Color = "#36A2EB", Description = "Personal tasks and errands", CreatedAt = fixedDate, UpdatedAt = fixedDate },
            new { Id = Guid.Parse("c3d4e5f6-a7b8-9012-cdef-123456789012"), Name = "Shopping", Icon = "fas fa-shopping-cart", Color = "#FFCE56", Description = "Shopping lists and purchases", CreatedAt = fixedDate, UpdatedAt = fixedDate },
            new { Id = Guid.Parse("d4e5f6a7-b8c9-0123-def0-234567890123"), Name = "Health", Icon = "fas fa-heartbeat", Color = "#4BC0C0", Description = "Health and fitness tasks", CreatedAt = fixedDate, UpdatedAt = fixedDate },
            new { Id = Guid.Parse("e5f6a7b8-c9d0-1234-ef01-345678901234"), Name = "Learning", Icon = "fas fa-book", Color = "#9966FF", Description = "Learning and education goals", CreatedAt = fixedDate, UpdatedAt = fixedDate }
        );
    }

    public override int SaveChanges()
    {
        UpdateTimestamps();
        return base.SaveChanges();
    }

    public override Task<int> SaveChangesAsync(CancellationToken cancellationToken = default)
    {
        UpdateTimestamps();
        return base.SaveChangesAsync(cancellationToken);
    }

    private void UpdateTimestamps()
    {
        var entries = ChangeTracker.Entries()
            .Where(e => e.State == EntityState.Added || e.State == EntityState.Modified);

        foreach (var entry in entries)
        {
            if (entry.Entity is TaskItem || entry.Entity is Category)
            {
                if (entry.State == EntityState.Added)
                {
                    entry.Property("CreatedAt").CurrentValue = DateTime.UtcNow;
                }
                entry.Property("UpdatedAt").CurrentValue = DateTime.UtcNow;
            }
        }
    }
}
