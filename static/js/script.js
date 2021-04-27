function search(n) {
	let query = document.getElementById("query-" + n).value.trim();
	location.href = "/search/" + query;
}
