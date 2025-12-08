document.addEventListener('DOMContentLoaded', () => {
    // Function to handle adding a movie to the watchlist
    const addMovieForm = document.getElementById('add-movie-form');
    if (addMovieForm) {
        addMovieForm.addEventListener('submit', async (event) => {
            event.preventDefault();
            const formData = new FormData(addMovieForm);
            const movieData = {
                title: formData.get('title'),
                year: formData.get('year'),
                genre: formData.get('genre'),
                description: formData.get('description'),
            };

            // Send movie data to the server
            const response = await fetch('/add_movie', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(movieData),
            });

            if (response.ok) {
                // Clear the form and show success message
                addMovieForm.reset();
                alert('Movie added successfully!');
            } else {
                alert('Failed to add movie. Please try again.');
            }
        });
    }

    // Function to handle deleting a movie from the watchlist
    const deleteButtons = document.querySelectorAll('.delete-movie');
    deleteButtons.forEach(button => {
        button.addEventListener('click', async () => {
            const movieId = button.dataset.movieId;

            const response = await fetch(`/delete_movie/${movieId}`, {
                method: 'DELETE',
            });

            if (response.ok) {
                // Remove the movie from the DOM
                button.closest('.movie-item').remove();
                alert('Movie deleted successfully!');
            } else {
                alert('Failed to delete movie. Please try again.');
            }
        });
    });
});