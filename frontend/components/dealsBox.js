export default function DealsBox({deal}){
    return (
        <>
        <ul>
            <li><b>{deal.client}</b> ({deal.value}), status : {deal.status}</li>
        </ul>
        </>
    )
}