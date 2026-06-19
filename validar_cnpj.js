function validarCNPJ(cnpj) {
    // Remove tudo que não for número
    cnpj = cnpj.replace(/\D/g, '');

    // Deve possuir 14 dígitos
    if (cnpj.length !== 14) {
        return false;
    }

    // Rejeita sequências iguais (000..., 111..., etc)
    if (/^(\d)\1{13}$/.test(cnpj)) {
        return false;
    }

    // Primeiro dígito
    const pesos1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2];

    let soma = 0;

    for (let i = 0; i < 12; i++) {
        soma += Number(cnpj[i]) * pesos1[i];
    }

    let resto = soma % 11;
    const digito1 = resto < 2 ? 0 : 11 - resto;

    // Segundo dígito
    const pesos2 = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2];

    soma = 0;

    const cnpj13 = cnpj.substring(0, 12) + digito1;

    for (let i = 0; i < 13; i++) {
        soma += Number(cnpj13[i]) * pesos2[i];
    }

    resto = soma % 11;
    const digito2 = resto < 2 ? 0 : 11 - resto;

    return cnpj.endsWith(`${digito1}${digito2}`);
}