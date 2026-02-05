const baiCon = document.querySelectorAll("[data-file]");
const noidung = document.getElementById("noidung");
const loop = document.getElementById("loop");
const vonglap = document.getElementById("vonglap");

/* click load bài */
baiCon.forEach(item => {
  item.addEventListener("click", () => {
    const file = item.dataset.file;
    console.log("Load:", file);

    fetch(file)
      .then(res => {
        if (!res.ok) throw new Error("Không tìm thấy file");
        return res.text();
      })
      .then(data => {
        noidung.innerHTML = `<pre>${data}</pre>`;
      })
      .catch(err => {
        noidung.innerHTML = "❌ Không load được file!";
        console.error(err);
      });
  });
});

/* mở / đóng menu vòng lặp */
loop.onclick = () => {
  vonglap.style.display =
    vonglap.style.display === "block" ? "none" : "block";
};
