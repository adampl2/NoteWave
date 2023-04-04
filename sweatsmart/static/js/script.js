function deleteNote(noteId) {
  const confirmed = confirm("Are you sure you want to delete this note?");
  if (!confirmed) return;
  fetch("/delete-note?confirm=yes", {
    method: "POST",
    body: JSON.stringify({ noteId: noteId }),
  }).then((_res) => {
    window.location.href = "/";
  });
}