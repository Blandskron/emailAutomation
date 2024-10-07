const express = require('express');
const bodyParser = require('body-parser');
const nodemailer = require('nodemailer');

const app = express();
app.use(bodyParser.json());

// Configuración de Nodemailer con SMTP de cPanel
const transporter = nodemailer.createTransport({
    host: 's320.v2nets.com', // Host del servidor SMTP de cPanel
    port: 465, // Puerto SMTP (465 para SSL)
    secure: true, // true para SSL
    auth: {
        user: 'eventounestadodigital@unestadodigital.cl',
        pass: '!XDOr^r&)stg'
    }
});


// Función para enviar el correo
const sendMail = async ({ to, subject, message }) => {
    const mailOptions = {
        from: 'eventounestadodigital@unestadodigital.cl',
        to: to,
        subject: subject,
        html: message,
    };

    try {
        const result = await transporter.sendMail(mailOptions);
        console.log('Email sent:', result);
        return result;
    } catch (error) {
        console.error('Error sending email:', error);
        throw error;
    }
};

app.post('/send-email', (req, res) => {
    const { to, subject, message } = req.body;

    sendMail({ to, subject, message })
        .then(response => res.status(200).send({ status: 'Email sent', to, subject, message }))
        .catch(error => res.status(500).send({ status: 'Failed to send email', to, subject, message, error: error.toString() }));
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});