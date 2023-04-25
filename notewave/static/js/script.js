document.addEventListener('DOMContentLoaded', function () {
  
  /** Hides flash message after 5 seconds of inactivity */

  setTimeout(function () {
    $('#flashMessage').fadeOut(1500, "linear");
  }, 5000);

  /** Gets the current year to display it in the footer element */

  document.getElementById("year").innerHTML = new Date().getFullYear();
});

/** Shows the modal and deletes the note from the database  */

function showConfirmDeleteModal(noteId) {
  let deleteUrl = "/delete-note/" + noteId;
  $('#delete-confirm-button').attr('href', deleteUrl);
  $('#confirmDeleteModal').modal('show');
}







