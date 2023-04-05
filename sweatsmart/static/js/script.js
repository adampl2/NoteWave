function showConfirmDeleteModal(noteId) {
  let deleteUrl = "/delete-note/" + noteId;
  $('#delete-confirm-button').attr('href', deleteUrl);
  $('#confirmDeleteModal').modal('show');
}





