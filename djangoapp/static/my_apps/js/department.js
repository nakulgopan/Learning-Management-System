function loadContent(section) {
    // Static content to be injected directly
    let content = {
        'vision': `
            <div class="content-box">
                <h2 onclick="toggleMission()" style="cursor:pointer; background:black; color:white;">Vision & Mission</h2>
                <div id="mission-content" style="display:block;">
                    <h3>Vision</h3>
                    <p>To be a Centre of Excellence in Civil Engineering by imparting quality education and research that nourishes the students to be leaders and innovators to serve for the betterment of society.</p>
                    <h3>Mission</h3>
                    <ul>
                        <li><strong>M1:</strong> To equip students with advanced knowledge in Civil Engineering, versatility, and an inquisitive attitude to explore innovative solutions for the betterment of society.</li>
                        <li><strong>M2:</strong> To provide undergraduate research experiences to address challenges in civil engineering and disseminate this knowledge at national and international venues.</li>
                        <li><strong>M3:</strong> To constantly update emerging technologies in the field of civil engineering through industry-institute interaction.</li>
                    </ul>
                </div>
            </div>`,
        'hod': `
            <div class="content-box">
               <div class="card" style="width: 18rem;">
  <img class="card-img-top" src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRlsLdW9xhqrCG4id9jVstuJT_e6HoxJdo5-A&s" alt="Card image cap">
  <div class="card-body">
    <h5 class="card-title">Card title</h5>
    <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
    <a href="#" class="btn btn-primary">Go somewhere</a>
  </div>
            </div>`,
        'facilities': `
            <div class="content-box">
                <h2>Facilities</h2>
                <p>State-of-the-art laboratories and classrooms...</p>
            </div>`,
        'publications': `
                <div class="content-box">
                <h2>Publications</h2>
                <p>Our graduates are placed in top companies...</p>
            </div>`,
        'placement': `
            <div class="content-box">
                <h2>Placement</h2>
                <p>Our graduates are placed in top companies...</p>
            </div>`,
        'clubs':`
        <div class="content box>
        <h2>HOD</h2>
        </div>`,
        'events': `
            <div class="content-box">
                <h2>Events</h2>
                <p>Annual technical fest and seminars...</p>
            </div>`,
        
        
    };
   
    // If the section exists in the content object, load it. Otherwise, show an error message.
    document.getElementById("main-content").innerHTML = content[section] || `
        <div class='content-box'>
            <h2>Error</h2>
            <p>Content not found. Please select a valid section.</p>
        </div>`;
}

// Function to toggle Vision & Mission sub-content
function toggleMission() {
    let missionDiv = document.getElementById("mission-content");
    if (missionDiv) {
        missionDiv.style.display = missionDiv.style.display === "none" ? "block" : "none";
    }
}
$('#myModal').on('shown.bs.modal', function () {
    $('#myInput').trigger('focus')
  })


