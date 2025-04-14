'use client'
import { useEffect, useState } from "react";
import {  useSearchParams } from "next/navigation";
import ClientBox from "../components/clientBox";
import DealsBox from "../components/dealsBox";

export default function UsersPage(){
    const params = useSearchParams();
    const userID = params.get('id'); 

    const [user, setUsers] = useState([]);
    const [skills, setSkills] = useState([]);
    const [deals, setDeals] = useState([]);
    const [clients, setClients] = useState([]);

    const [loading, setLoading] = useState(true);
    useEffect(() => {
        fetch("http://localhost:8000/api/user/"+ userID )
            .then((res) => res.json())
            .then((data) => {
                setUsers(data || {});
                setSkills(data.skills || []);
                setDeals(data.deals || []);
                setClients(data.clients || []);
                setLoading(false);
            })
            .catch((err) => {
                console.error("Failed to fetch data:", err);
                setLoading(false);
            });
      }, [params]);

    return (
        <>
        <div style={{ padding: "2rem" }}>
            <h1>Detail for user {user.name}</h1>
            <h3>Role: {user.role}</h3>
            <h5>on region {user.region}</h5>

        {
            loading ? (<p>Loading...</p>) : 
            (<div><b>Skills : </b> {skills.join(', ')} </div> )
        }
        {
            loading ? (<p>Loading...</p>) : 
            (<div><b>Clients : </b> 
                {clients.map((client,index)=>
                (
                    <ClientBox key={index} client={client}/> 
                ))
                }  
            </div>)
        }
        {
            loading ? (<p>Loading...</p>) : 
            (<div><b>Deals : </b> 
                {deals.map((deal,index)=>
                (
                    <DealsBox key={index} deal={deal}/> 
                ))
                }  
            </div>)
        }
        </div>
        </>
    )
}