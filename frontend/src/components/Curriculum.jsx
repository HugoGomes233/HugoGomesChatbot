import "./Curriculum.css";

// Curriculum component renders Hugo's CV layout with sidebar and main content
export default function Curriculum() {
  return (
    <div className="cv-layout">
      {/* Sidebar containing profile picture, personal data, and social links */}
      <aside className="cv-sidebar">
        <div className="sidebar-section">
          <img
            src="/personal_data_picture.jpg"
            alt="Hugo dos Santos Gomes"
            className="profile-pic"
          />
        </div>
        <div className="sidebar-section">
          <h2>Personal Data</h2>
          <ul className="personal-data">
            <li><span>Full Name:</span><span>Hugo dos Santos Gomes</span></li>
            <li><span>Phone:</span><span>+351 925 733 753</span></li>
            <li><span>Address:</span><span>Figueira da Foz, Portugal</span></li>
            <li><span>Email:</span><span><a href="mailto:hugomes1999@gmail.com">hugomes1999@gmail.com</a></span></li>
            <li><span>Date of Birth:</span><span>09-09-1999</span></li>
            <li><span>Nationality:</span><span>Portuguese</span></li>
            <li><span>Driver’s License:</span><span>A1, A2, B</span></li>
            <li><span>Languages:</span><span>Portuguese, English</span></li>
          </ul>
          <div className="sidebar-links">
            <a
              href="https://linkedin.com/in/hugo-gomes-49476a22b"
              target="_blank"
              rel="noreferrer"
            >
              <img
                src="/linkedin.png"
                alt="LinkedIn"
                className="sidebar-icon"
              />
            </a>

            <a
              href="https://github.com/HugoGomes233"
              target="_blank"
              rel="noreferrer"
            >
              <img
                src="/github.png"
                alt="GitHub"
                className="sidebar-icon"
              />
            </a>
          </div>

        </div>
      </aside>

      {/* Main content area */}
      <main className="cv-main">
        <header className="cv-header">
          <h1>Hugo dos Santos Gomes</h1>
          <p className="subtitle">Software Developer</p>
        </header>

        {/* About Me section */}
        <section>
          <h2>About Me</h2>
          <p>

            Passionate Developer with 3 years of experience turning ideas into functional applications. I began my career
            with OutSystems, where I built a solid foundation in software development, working in subcontracting projects
            with Deloitte and Noesis. Today, my growing passion for Generative AI is driving my career pivot. Skilled in
            problem-solving, collaboration, and adapting to new technologies, I am eager to apply my technical background
            and curiosity to build innovative AI-driven solutions and continue expanding my expertise in this fast-evolving
            field.
          </p>
        </section>

        {/* Professional Experience */}
        <section>
          <h2>Professional Experience</h2>

          <div className="job">
            <div className="job-head">
              <h3>Web & Low-Code Developer </h3>
              <span className="date">Itglee Consultant (May 2022 – Jun. 2025 )</span>
            </div>

            {/* Assignment 1 */}
            <div className="assignment">
              <h4>AngularJS / Node.js Developer <span className="dim">(3 months)</span></h4>
              <p className="muted">Partner: <strong>Noesis</strong> · Client: <strong>Santander</strong></p>
              <ul className="bulleted">
                <li>Collaborated with cross-functional teams to design and implement reactive front-end features using
                  Angular, RxJS, and Signal Store. The application was developed to manage permissions and certificates for
                  technical and functional applications, ensuring security and operational efficiency. I contributed by applying
                  best practices in TypeScript development, version control, and defect resolution, while ensuring
                  maintainability, scalability, and performance within Agile workflows. </li>
              </ul>
              <p className="tech"><span>Technologies:</span> HTML · CSS · AngularJS · JavaScript · TypeScript · Git · GitHub · Microsoft Planner · Postman</p>
            </div>

            {/* Assignment 2 */}
            <div className="assignment">
              <h4>ReactJS / Node.js Developer <span className="dim">(5 months)</span></h4>
              <p className="muted">Client: <strong>Travel Agency Belle Epoque</strong> · Project: <strong>Backoffice Internal Management Application</strong></p>
              <ul className="bulleted">
                <li>In this project, I designed and delivered a full-stack solution for managing client data, quote requests, and
                  file storage. I integrated Google Drive to automate workflows and improved internal efficiency through a
                  modern, responsive interface. I collaborated closely with the team in an Agile environment, contributing to
                  planning, sprint execution, and defect resolution</li>
              </ul>
              <p className="tech"><span>Technologies:</span> HTML · TailwindCSS · React JS · Node JS · AWS DynamoDB · JavaScript · Git · GitHub · Agile · Jira</p>
            </div>

            {/* Assignment 3 */}
            <div className="assignment">
              <h4>OutSystems Reactive Developer <span className="dim">(2 years – 2 months)</span></h4>
              <p className="muted">Partner: <strong>Deloitte</strong> · Client: <strong>PPL Next Gen</strong></p>
              <ul className="bulleted">
                <li>A digital-first electronic trading platform for the London insurance market, designed to modernize and
                  streamline broker–underwriter interactions. I was responsible for requirement analysis and development, as
                  well as resolving both production and development defects in close collaboration with the testing team,
                  alongside performance optimization. Working within Agile sprints, I contributed to delivering a scalable,
                  intuitive, and high-quality platform that enhanced efficiency and reliability across the market. </li>
              </ul>
              <p className="tech"><span>Technologies:</span> OutSystems · Agile · Jira · MongoDB · Azure DevOps · Postman</p>
            </div>

            <div className="assignment">
              <h4>Internship — OutSystems Web Developer <span className="dim">(6 months)</span></h4>
              <ul className="bulleted">
                <li>I began as an OutSystems Web Developer Intern, where I learned the platform and developed a training
                  reactive web application for hotel bookings, gaining hands-on experience in SQL, Agile methodologies, and
                  Scrum.</li>
              </ul>
              <p className="tech"><span>Technologies:</span> OutSystems · Agile · Jira · MongoDB · Azure DevOps · Postman</p>
            </div>
          </div>
        </section>

        {/* Education */}
        <section>
          <h2>Education</h2>
          <p><strong>Software Engineering Degree</strong></p>
          <p className="muted">Instituto Politécnico de Portalegre (2018–2021)</p>
        </section>

        {/* Software Skills */}
        <section>
          <h2>Software Skills</h2>

          <div className="skills-grid">
            <div className="skill-block">
              <h4>Gen AI</h4>
              <p>LangChain, LangGraph, Azure OpenAI</p>
            </div>

            <div className="skill-block">
              <h4>Platforms</h4>
              <p>OutSystems (Service Studio, Service Center, Mentor AI), Firebase</p>
            </div>

            <div className="skill-block">
              <h4>Programming Languages</h4>
              <p>Python (pandas, numpy, matplotlib), C, HTML, CSS, TailwindCSS, JavaScript/TypeScript (AngularJS, ReactJS, NodeJS)</p>
            </div>

            <div className="skill-block">
              <h4>Database</h4>
              <p>MongoDB, SQL, DynamoDB, OracleDB</p>
            </div>

            <div className="skill-block">
              <h4>Version Control</h4>
              <p>Git (GitHub)</p>
            </div>

            <div className="skill-block">
              <h4>API Tools</h4>
              <p>Postman</p>
            </div>

            <div className="skill-block">
              <h4>Cloud</h4>
              <p>Azure</p>
            </div>

            <div className="skill-block">
              <h4>Containerization</h4>
              <p>Docker</p>
            </div>
          </div>
        </section>
        {/* Certifications */}
        <section>
          <h2>Certifications & Courses</h2>
          <ul className="bulleted">
            <li>LangGraph Academy: Foundation (Ago 2025)</li>
            <li>Coursera: Python for Data Science & AI (Ago 2025)</li>
            <li>OutSystems Architecture Specialist (Set 2024)</li>
            <li>OutSystems Developer ODC (May 2023)</li>
            <li>OutSystems Mobile Developer Specialist (Nov 2022)</li>
            <li>OutSystems Associate Reactive Developer (Jun 2022)</li>
            <li>CCNA Routing & Switching: Scaling Networks (Jan 2021)</li>
            <li>CCNA Routing & Switching: Essentials (Set 2020)</li>
            <li>CCNA Introduction to Networks (Abr 2020)</li>
          </ul>
        </section>
      </main>
    </div>
  );
}
