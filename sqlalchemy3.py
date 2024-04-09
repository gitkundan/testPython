# Ingest data into the database
for item in json_data:
    physical_server = PhysicalServer(id=item['physical_server_id'])
    if 'virtual_platform' in item:
        virtual_platform_data = item['virtual_platform']
        
        # Check if a similar virtual platform already exists
        existing_virtual_platform = session.query(VirtualPlatform).filter_by(vp_id=virtual_platform_data['vp_id']).first()
        if existing_virtual_platform:
            # Link the existing virtual platform to the physical server
            physical_server.virtual_platform = existing_virtual_platform
        else:
            # Create a new virtual platform
            virtual_platform = VirtualPlatform(vp_id=virtual_platform_data['vp_id'])
            
            # Check if cluster data is present
            if 'cluster' in virtual_platform_data:
                cluster_data = virtual_platform_data['cluster']
                
                # Check if a similar cluster already exists
                existing_cluster = session.query(Cluster).filter_by(cluster_id=cluster_data['cluster_id']).first()
                if existing_cluster:
                    # Link the existing cluster to the new virtual platform
                    virtual_platform.cluster = existing_cluster
                else:
                    # Create a new cluster
                    cluster = Cluster(cluster_id=cluster_data['cluster_id'])
                    virtual_platform.cluster = cluster
            
            session.add(virtual_platform)
            physical_server.virtual_platform = virtual_platform

    session.add(physical_server)

session.commit()
