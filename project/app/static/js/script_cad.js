document.getElementById('cadastro-form').addEventListener('submit', function(event) {
    event.preventDefault(); // Impede o envio padrão do formulário

    // Coletar os dados do formulário
    const primeiroNome = document.getElementById('firstname').value;
    const sobrenome = document.getElementById('lastname').value;
    const email = document.getElementById('email').value;
    const celular = document.getElementById('number').value;
    const senha = document.getElementById('password').value;
    const confirmarSenha = document.getElementById('confirmPassword').value;
    const genero = document.querySelector('input[name="gender"]:checked');

    //coletar url
    const successUrl = document.body.getAttribute('data-success-url');
    console.log("Redirecionando para:", successUrl);

    // Validações adicionais
    if (!genero) {
        alert('Por favor, selecione um gênero.');
        return;
    }

    if (senha.length !== 12) {
        alert('A senha deve ter exatamente 12 caracteres!');
        return;
    }

    // Verifica se as senhas coincidem
    if (senha !== confirmarSenha) {
        alert('As senhas não coincidem!');
        return;
    }

    // Dados a serem enviados
    const data = {
        usuario: {
            nome: `${primeiroNome} ${sobrenome}`,
            email: email,
            telefone: celular,
            senha: senha,
            sexo: genero.value,  // Valor selecionado do gênero
        }
    };

    // Exibir no console os dados enviados (para debugging)
    console.log('Dados enviados:', JSON.stringify(data));

    // Enviar os dados para o backend
    fetch('/participantes/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': document.querySelector('input[name="csrfmiddlewaretoken"]').value,  // CSRF token
        },
        body: JSON.stringify(data),
    })
    .then(response => {
        if (!response.ok) {
            return response.json().then(err => {
                throw new Error(err.message || 'Erro no cadastro');
            });
        }
        return response.json();
    })
    .then(data => {
        alert('Cadastro realizado com sucesso!');  // Notifica o usuário
        document.getElementById('cadastro-form').reset();  // Limpar o formulário após sucesso
        setTimeout(() => {
            window.location.href = successUrl;  // Redirecionar após 1 segundo
        }, 1000); // Atraso de 1000 milissegundos (1 segundo)
    })
    .catch(error => {
        alert('Erro: ' + error.message);
    });
});
