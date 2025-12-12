using Microsoft.AspNetCore.Mvc.RazorPages;
using Microsoft.EntityFrameworkCore;
using TaskManager.Web.Data;

namespace TaskManager.Web.Pages;

public class IndexModel : PageModel
{
    private readonly TaskManagerContext _context;

    public IndexModel(TaskManagerContext context)
    {
        _context = context;
    }

    public int CategoryCount { get; set; }
    public int TaskCount { get; set; }
    public int PendingTaskCount { get; set; }
    public int CompletedTaskCount { get; set; }

    public async Task OnGetAsync()
    {
        CategoryCount = await _context.Categories.CountAsync();
        TaskCount = await _context.Tasks.CountAsync();
        PendingTaskCount = await _context.Tasks.CountAsync(t => 
            t.Status == Models.TaskStatus.Todo || t.Status == Models.TaskStatus.InProgress);
        CompletedTaskCount = await _context.Tasks.CountAsync(t => 
            t.Status == Models.TaskStatus.Done);
    }
}
