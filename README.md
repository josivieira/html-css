<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>Conecta+ - Login</title>
<style>
  /* Reset básico */
  * {
    box-sizing: border-box;
  }
  body {
    margin: 0;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    color: #333;

    /* Background image with dark overlay */
    background: 
      linear-gradient(rgba(44, 62, 80, 0.7), rgba(44, 62, 80, 0.7)),
      url('https://images.unsplash.com/photo-1504384308090-c894fdcc538d?auto=format&fit=crop&w=1470&q=80') no-repeat center center fixed;
    background-size: cover;
  }
  .login-container {
    background: rgba(255, 255, 255, 0.95);
    width: 360px;
    padding: 40px 30px;
    border-radius: 12px;
    box-shadow: 0 8px 24px rgba(0,0,0,0.15);
    text-align: center;
  }
  .login-container h1 {
    margin-bottom: 10px;
    color: #2c3e50;
    font-weight: 700;
    font-size: 2.2rem;
  }
  .login-container p {
    margin-bottom: 30px;
    color: #7f8c8d;
    font-size: 1rem;
  }
  form {
    text-align: left;
  }
  label {
    display: block;
    font-weight: 600;
    margin-bottom: 8px;
    font-size: 0.9rem;
    color: #34495e;
  }
  input[type="email"],
  input[type="password"],
  select {
    width: 100%;
    padding: 12px 14px;
    margin-bottom: 20px;
    border-radius: 8px;
    border: 1.8px solid #bdc3c7;
    font-size: 1rem;
    transition: border-color 0.2s ease-in-out;
  }
  input[type="email"]:focus,
  input[type="password"]:focus,
  select:focus {
    border-color: #2980b9;
    outline: none;
  }
  button {
    background: #27ae60;
    color: white;
    font-weight: 600;
    border: none;
    width: 100%;
    padding: 14px;
    font-size: 1.1rem;
    border-radius: 10px;
    cursor: pointer;
    transition: background-color 0.3s ease;
  }
  button:hover {
    background: #229954;
  }
  .footer-links {
    margin-top: 20px;
    text-align: center;
  }
  .footer-links a {
    color: #2980b9;
    text-decoration: none;
    font-size: 0.95rem;
    margin: 0 12px;
  }
  .footer-links a:hover {
    text-decoration: underline;
  }
  /* Responsive */
  @media (max-width: 400px) {
    .login-container {
      width: 90%;
      padding: 25px 20px;
    }
  }
  .sr-only{
    position:absolute;
    width:1px;
    height:1px;
    padding:0;
    margin:-1px;
    overflow:hidden;
    clip:rect(0,0,0,0);
    border:0;
  }
</style>
</head>
<body>
  <section class="login-container" aria-label="Área de login Conecta+">
    <h1>Conecta+</h1>
    <p>Conectando pessoas e empresas para um impacto social positivo.</p>
    <form id="loginForm" aria-describedby="login-instructions">
      <label for="user-type">Eu sou:</label>
      <select name="user-type" id="user-type" required aria-required="true" aria-describedby="type-desc">
        <option value="" disabled selected>Selecione uma opção</option>
        <option value="pessoa">Pessoa</option>
        <option value="empresa">Empresa</option>
      </select>
      <span id="type-desc" class="sr-only">Selecione se você está logando como pessoa ou empresa.</span>

      <label for="email">E-mail</label>
      <input type="email" id="email" name="email" placeholder="seuemail@exemplo.com" required aria-required="true" autocomplete="email"/>

      <label for="password">Senha</label>
      <input type="password" id="password" name="password" placeholder="Digite sua senha" required aria-required="true" autocomplete="current-password"/>

      <button type="submit" aria-label="Entrar na plataforma Conecta+">Entrar</button>
    </form>

    <div class="footer-links">
      <a href="#" aria-label="Criar conta no Conecta+">Criar uma conta</a>
      <a href="#" aria-label="Esqueci minha senha">Esqueceu a senha?</a>
    </div>
  </section>

<script>
  document.getElementById('loginForm').addEventListener('submit', function(e) {
    e.preventDefault();
    const userType = document.getElementById('user-type').value;
    const email = document.getElementById('email').value.trim();

    if(!userType) {
      alert('Por favor, selecione o tipo de usuário.');
      return;
    }
    if(!email) {
      alert('Por favor, insira um e-mail válido.');
      return;
    }
    // Simular autenticação / registro bem-sucedido
    // Armazena dados no localStorage para o próximo passo
    localStorage.setItem('conectaplus_userType', userType);
    localStorage.setItem('conectaplus_email', email);

    // Redireciona para página do perfil
    window.location.href = 'conecta-plus-profile.html';
  });
</script>
</body>
</html>


