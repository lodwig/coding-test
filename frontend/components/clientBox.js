export default function ClientBox({client}){
    return (
        <>
        <ul>
            <li><b>{client.name}</b> ({client.industry}), Contact : {client.contact}</li>
        </ul>
        </>
    )
}