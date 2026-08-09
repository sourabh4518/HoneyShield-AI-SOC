from fpdf import FPDF

class PresentationPDF(FPDF):
    def header(self):
        self.set_fill_color(30, 41, 59)
        self.rect(0, 0, 297, 18, 'F')
        self.set_font('Helvetica', 'B', 12)
        self.set_text_color(255, 255, 255)
        self.cell(0, 2, 'HoneyShield: Real-Time IoT AI SOC Threat Intelligence System', align='C', ln=1)
        self.ln(6)

    def footer(self):
        self.set_y(-12)
        self.set_font('Helvetica', 'I', 8)
        self.set_text_color(148, 163, 184)
        self.cell(0, 10, f'Slide {self.page_no()} of 4 | HoneyShield Technical Presentation', align='C')

def create_slides():
    pdf = PresentationPDF(orientation='L', unit='mm', format='A4')
    pdf.set_auto_page_break(auto=True, margin=15)

    # --- SLIDE 1 ---
    pdf.add_page()
    pdf.set_font('Helvetica', 'B', 16)
    pdf.set_text_color(30, 41, 59)
    pdf.cell(0, 10, 'Slide 1: Project Overview & Core Problem Statement', ln=1)
    pdf.line(10, 32, 287, 32)
    pdf.ln(4)

    pdf.set_font('Helvetica', 'B', 11)
    pdf.cell(0, 6, 'Problem Statement:', ln=1)
    pdf.set_font('Helvetica', '', 10)
    pdf.multi_cell(0, 5, '- IoT infrastructure faces continuous brute-force probes and automated malware scripts.\n- Raw Cowrie honeypot logs (cowrie.json) are dense, unstructured, and massive—making manual threat analysis impossible for SOC analysts.')
    pdf.ln(3)

    pdf.set_font('Helvetica', 'B', 11)
    pdf.cell(0, 6, 'HoneyShield Solution:', ln=1)
    pdf.set_font('Helvetica', '', 10)
    pdf.multi_cell(0, 5, '- Integrates Cowrie Honeypot, an automated 15-second polling pipeline, Multi-Class ML classification, Google Gemini LLM summarization, and an interactive Streamlit SOC Dashboard into a unified threat intelligence platform.')

    # --- SLIDE 2 ---
    pdf.add_page()
    pdf.set_font('Helvetica', 'B', 16)
    pdf.set_text_color(30, 41, 59)
    pdf.cell(0, 10, 'Slide 2: System Architecture & Technical Stack', ln=1)
    pdf.line(10, 32, 287, 32)
    pdf.ln(4)

    pdf.set_font('Helvetica', 'B', 11)
    pdf.cell(0, 6, 'Data Pipeline Flow:', ln=1)
    pdf.set_font('Helvetica', '', 10)
    pdf.multi_cell(0, 5, '1. Acquisition: Cowrie SSH/Telnet Honeypot captures unauthorized attacker sessions.\n2. Daemon Pipeline: auto_update.py polls logs every 15s and executes parse_all.py.\n3. Persistence: Processed records, ML confidence, and GeoIP metadata saved in SQLite3 (honeyshield.db).')
    pdf.ln(3)

    pdf.set_font('Helvetica', 'B', 11)
    pdf.cell(0, 6, 'Technology Stack:', ln=1)
    pdf.set_font('Helvetica', '', 10)
    pdf.multi_cell(0, 5, '- OS: Kali Linux | Language: Python 3 | Honeypot: Cowrie\n- Storage: SQLite3 | Analytics: Pandas, NumPy, Scikit-Learn\n- Frontend & Maps: Streamlit, Plotly Express | AI: Google Gemini API | PDF: FPDF')

    # --- SLIDE 3 ---
    pdf.add_page()
    pdf.set_font('Helvetica', 'B', 16)
    pdf.set_text_color(30, 41, 59)
    pdf.cell(0, 10, 'Slide 3: AI Engine & Advanced Threat Intelligence', ln=1)
    pdf.line(10, 32, 287, 32)
    pdf.ln(4)

    pdf.set_font('Helvetica', 'B', 11)
    pdf.cell(0, 6, 'Core AI & Analytics Features:', ln=1)
    pdf.set_font('Helvetica', '', 10)
    pdf.multi_cell(0, 5, '- ML Threat Classifier: Evaluates raw shell commands into 8 attack categories with exact confidence scores.\n- MITRE ATT&CK Mapping: Automatically tags commands to official MITRE tactics/techniques via mitre_mapper.py.\n- LLM Incident Summarizer: Uses Google Gemini API to write a 2-sentence executive threat summary.\n- Live GeoIP Attack Map: Resolves attacker IPs to Country and City coordinates on a Plotly interactive world map.')

    # --- SLIDE 4 ---
    pdf.add_page()
    pdf.set_font('Helvetica', 'B', 16)
    pdf.set_text_color(30, 41, 59)
    pdf.cell(0, 10, 'Slide 4: SOC Dashboard Capabilities & Operations', ln=1)
    pdf.line(10, 32, 287, 32)
    pdf.ln(4)

    pdf.set_font('Helvetica', 'B', 11)
    pdf.cell(0, 6, 'Dashboard Features:', ln=1)
    pdf.set_font('Helvetica', '', 10)
    pdf.multi_cell(0, 5, '- Real-Time Metrics: Live cards for Total Attacks, Unique IPs, Top Threat Category, and Avg Confidence.\n- Time Window Filters: View Historical, Today (Last 24 Hours), or Latest (Last 1 Hour) views.\n- Live Attack Logs Table: Real-time table displaying ID, Timestamp (IST), IP, Country, City, Command, MITRE Code, Threat Category, and Confidence.\n- Reporting & System Controls: FPDF threat intelligence export and database reset management.')

    pdf.output('HoneyShield_Presentation_4Slides.pdf')
    print('✅ HoneyShield_Presentation_4Slides.pdf generated successfully!')

if __name__ == '__main__':
    create_slides()
